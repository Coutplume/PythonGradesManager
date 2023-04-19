import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Login from '@/components/Login'
import ControlTab from '@/components/ControlTab'
import Admin from '@/components/Admin'

import CourseManage from '@/components/children/CourseManage'
import FacultyManage from '@/components/children/FacultyManage'
import StudentManage from '@/components/children/StudentManage'
import GradesManage from '@/components/children/GradesManage'
import GradesUpload from '@/components/children/GradesUpload'
import GradesAnalyse from '@/components/children/GradesAnalyse'
import QueueManage from '@/components/children/QueueManage'
import ClassManage from '@/components/children/ClassManage'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path:'/',
      redirect: '/login'
    },
    {
      path:'/login',
      name:'Login',
      component: Login
    },
    {
      path:'/controlTab',
      name:'ControlTab',
      component: ControlTab,
      children: [
        {
          path: 'gradesManage',
          name: 'GradesManage',
          component: GradesManage
        },
        {
          path: 'gradesUpload',
          name: 'GradesUpload',
          component: GradesUpload
        },
        {
          path: 'analyse',
          name: 'Analyse',
          component: GradesAnalyse
        }
      ]
    },
    {
      path:'/admin',
      name:'Admin',
      component: Admin,
      children:[
        {
          path:'courseManage',
          name:'CourseManage',
          component: CourseManage
        },
        {
          path:'facultyManage',
          name:'FacultyManage',
          component: FacultyManage
        },
        {
          path:'studentManage',
          name:'StudentManage',
          component: StudentManage
        },
        {
          path:'queueManage',
          name:'QueueManage',
          component: QueueManage
        },
        {
          path:'classManage',
          name: 'ClassManage',
          component: ClassManage
        }
      ]
    }
  ]
})
