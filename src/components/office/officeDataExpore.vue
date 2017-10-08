<template>
    <div>
        <el-row style="margin-top:50px" :gutter="40" justify>
            <el-col :span="5" :offset="6">
                <el-input placeholder="请输入搜索关键字" icon="search" v-model="inputDataForSearch" :on-icon-click="filterByInputDataForSearch" @keyup.enter.native="filterByInputDataForSearch">
                </el-input>
            </el-col>
            <el-col :span="3">
                <div style="display: flex">
                    <el-button type="primary" icon="search" @click="filterByInputDataForSearch" :loading="loadingButton">搜 索
                    </el-button>
                    <el-button type="primary" icon="delete" @click="delInputDataForSearch">清空条件</el-button>
                    <el-button type="primary" icon="document" @click="excelExport">导出数据</el-button>
                </div>
            </el-col>
        </el-row>
        <el-row style="margin-top:30px">
            <el-col :span="22" :offset="1">
                <el-table id="expore-table" :data="tableInfoShow['data']" style="width: 100%" highlight-current-row v-loading.body="loadingTable" fit height="550">
                    <template v-for="(item, index) in tableInfoShow['colName']">
                        <el-table-column :prop="tableInfoShow['propName'][index]" :label="item" :key="item.key" v-if="tableInfoShow['propName'][index]!='state'" align='center'>
                        </el-table-column>
                        <el-table-column :prop="tableInfoShow['propName'][index]" :label="item" :key="item.key" v-else align='center'>
                            <template scope="scope">
                                <el-tag :color="tableRowStyle(scope.row)" close-transition>{{scope.row.state}}</el-tag>
                            </template>
                        </el-table-column>
                    </template>
                </el-table>
            </el-col>
        </el-row>
        <el-row style="margin-top:30px">
            <el-col :span="22" :offset="1">
                <el-pagination @current-change="handleCurrentChange" :current-page.sync="currentPage2" :page-size="10" layout="prev, pager, next, jumper" :total="stuNum" style="float:right">
                </el-pagination>
            </el-col>
        </el-row>
    </div>
</template>

<script>

import { officeDataExpore, JSONToExcelConvertor } from '@/api/api'

export default {
    data() {
        return {
            currrentPage2: 1,
            tableInfoTotal: '',
            tableInfoTemp: '',
            tableInfoShow: { data: [] },
            elements: {},
            iconClassMouseMove: 'fa fa-search fa-2x txt-blue cur-icon',
            iconClassMouseOut: 'fa fa-search fa-lg txt-blue',
            inputDataForSearch: '',
            searchKey: '',
            loadingTable: false,
            loadingButton: false,
            stuNum: 0,
        }
    },
    directives: {
        //将该dom注册进this中
        run(el, binding) {
            if (typeof binding.value == 'function')
                binding.value(el);
        }
    },
    methods: {
        handleCurrentChange(val) {
            this.tableInfoShow['data'] = []
            for (var i = 0; i < 10; i++) {
                this.tableInfoShow['data'].push()
            }
            var j = 0
            for (var i = (val - 1) * 10; i < (val - 1) * 10 + 10 && i < this.stuNum; i++ , j++) {
                this.$set(this.tableInfoShow['data'], j, this.tableInfoTemp['data'][i])
            }
        },
        excelExport() {
            this.$prompt('请输入文件名', '提示', {
                confirmButtonText: '确定',
                cancelButtonText: '取消',
                inputValue: 'report',
                inputErrorMessage: '',
                inputValidator: this.judgeMessageIfEmpty,
            }).then(({ value }) => {
                let data = { "title": this.tableInfoShow['colName'], "data": [] }
                for (var dataIndex in this.tableInfoShow['data']) {
                    data['data'].push([])
                    for (var name in this.tableInfoShow['propName']) {
                        data['data'][dataIndex].push(this.tableInfoShow['data'][dataIndex][this.tableInfoShow['propName'][name]])
                    }
                }
                if (data == '')
                    return
                JSONToExcelConvertor(data.data, value, data.title)
                this.$notify.success({
                    title: '消息',
                    message: '导出成功'
                })
            }).catch(() => {
                this.$notify.info({
                    title: '消息',
                    message: '取消输入'
                })
            });
        },
        judgeMessageIfEmpty(value) {
            if (value.length == 0) {
                return "文件名不能为空"
            }
            return true
        },
        getTableInfo() {
            return getIndexTableInfo()
        },
        tableRowStyle(row) {
            if (row['state'] == '推介关注') {
                return '#F7BA2A'
            } else if (row['state'] == '重点关注') {
                return '#FF4949'
            } else if (row['state'] == '毕业') {
                return '#13CE66'
            }
            return '#1D8CE0'
        },
        changeIcon(mode, index) {
            let refValue = 'icon' + index
            if (mode == 0) {
                //this.iconClass = "fa fa-search fa-2x txt-blue"
                this.elements[refValue].className = this.iconClassMouseMove
            } else {
                //this.iconClass = "fa fa-search fa-lg txt-blue"
                this.elements[refValue].className = this.iconClassMouseOut
            }
        },
        handleEdit(index, row) {
            //console.log(index)
            //console.log(row)
        },
        register(index) {
            return (el) => {
                this.elements["icon" + index] = el;
            }
        },
        filterByInputDataForSearch() {
            //this.tableInfoShow = ''
            var index
            var indexProp
            var tableInfoShowTemp = JSON.parse(JSON.stringify(this.tableInfoTotal))
            var ifpush
            this.loadingButton = true
            tableInfoShowTemp['data'] = new Array()
            for (index in this.tableInfoTotal['data']) {
                ifpush = false
                for (indexProp in this.tableInfoTotal['propName']) {
                    if (this.tableInfoTotal['data'][index][this.tableInfoTotal['propName'][indexProp]].match(this.inputDataForSearch) != null) {
                        ifpush = true
                        break
                    }
                }
                if (ifpush == true) {
                    tableInfoShowTemp['data'].push(this.tableInfoTotal['data'][index])
                }
            }
            this.currentPage2 = 1
            this.tableInfoTemp = tableInfoShowTemp
            this.tableInfoShow['data'] = []
            this.stuNum = tableInfoShowTemp['data'].length
            for (var i = 0; i < 10 && i < this.stuNum; i++) {
                this.$set(this.tableInfoShow['data'], i, tableInfoShowTemp['data'][i])
            }
            //        this.tableInfoShow = tableInfoShowTemp
            this.loadingButton = false
        },
        delInputDataForSearch() {
            this.currrentPage2 = 1
            this.inputDataForSearch = ''
            this.tableInfoTemp = this.tableInfoTotal
            this.tableInfoShow['data'] = []
            this.stuNum = this.tableInfoTemp['data'].length
            for (var i = 0; i < 10 && i < this.stuNum; i++) {
                this.$set(this.tableInfoShow['data'], i, this.tableInfoTemp['data'][i])
            }
        }
    },
    mounted() {
        for (var i = 0; i < 10; i++) {
            this.tableInfoShow['data'].push()
        }
        //保存所有结果
        this.loadingTable = true
        let that = this
        officeDataExpore(this.$store.state.userid).then(
            (data) => {
                that.tableInfoTotal = data['data']
                that.tableInfoTemp = that.tableInfoTotal
                that.stuNum = that.tableInfoTotal['data'].length
                that.tableInfoShow['colName'] = that.tableInfoTotal['colName']
                that.tableInfoShow['propName'] = that.tableInfoTotal['propName']
                for (var i = 0; i < 10 && i < this.stuNum; i++) {
                    that.tableInfoShow['data'][i] = that.tableInfoTotal['data'][i]
                }
            }
        )
        this.loadingTable = false
        this.loadingButton = false
    },
}
</script>

<style scoped>
.txt-blue {
    color: #13CE66
}

.cur-icon {
    cursor: pointer;
}
</style>

