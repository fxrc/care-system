import Home from '@/home'
import Login from '@/components/login/login'
import IndexMajor from '@/components/index/indexMajor'
import indexStudents from '@/components/index/indexStudents'
import person from '@/components/index/personal'
import officeDataExpore from '@/components/office/officeDataExpore'
import officeSuggestions from '@/components/office/officeSuggestions'
import dataFilter from '@/components/office/dataFilter'
import systemUserTeam from '@/components/system/systemUserTeam'
import systemRoleTeam from '@/components/system/systemRoleTeam'
import systemUsers from '@/components/system/systemUsers'
import dataUpdateBasic from '@/components/data/dataUpdateBasic'
import dataUpdateScore from '@/components/data/dataUpdateScore'
import dataUpdateFocus from '@/components/data/dataUpdateFocus'


import store from '@/vuex/store'

let routes = [
  {
    path: '/',
    name: 'Login',
    component: Login
  },
  {
    path: '/login',
    name: '',
    component: Login
  },
  {
    path: '/home',
    name: 'Home',
    component: Home,
    children: [
            { path: '/indexMajor', component: IndexMajor, name: store['indexMajor'] },
            { path: '/indexStudents', component: indexStudents, name: store['indexStudents'] },
            { path: '/person', component: person, name: store['person'] },
            { path: '/officeDataExpore', component: officeDataExpore, name: store['officeDataExpore'] },
            { path: '/systemUserTeam', component: systemUserTeam, name: store['systemUserTeam'] },
            { path: '/systemRoleTeam', component: systemRoleTeam, name: store['systemRoleTeam'] },
            { path: '/systemUsers', component: systemUsers, name: store['systemUsers'] },
            { path: '/officeSuggestions', component: officeSuggestions, name: store['officeSuggestions'] },
            { path: '/dataUpdateBasic', component: dataUpdateBasic, name: store['dataUpdateBasic'] },
            { path: '/dataUpdateScore', component: dataUpdateScore, name: store['dataUpdateScore'] },
            { path: '/dataFilter', component: dataFilter, name: store['dataFilter'] },
            { path: '/dataUpdateFocus', component: dataUpdateFocus, name: store['dataUpdateFocus'] }
        ]
  }
]

export default routes;