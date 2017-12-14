<template>
  <div>
    <el-carousel height="600px">
      <el-carousel-item v-for="(item,index) in itemImg" :key="index">
        <img :src="item.img" width="100%">
      </el-carousel-item>
    </el-carousel>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        itemImg :[{img: 'http://www.hitwh.edu.cn/bg/xxs.jpg'},
          {img: 'http://www.hitwh.edu.cn/bg/gongyu.jpg'},
          {img: 'http://www.hitwh.edu.cn/bg/bg1.jpg'},
          {img: 'http://www.hitwh.edu.cn/bg/bg2.jpg'}]
      }
    }
  }
</script>



<style>

</style>
