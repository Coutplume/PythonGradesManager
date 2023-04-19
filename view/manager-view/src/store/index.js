import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const store = new Vuex.Store({
    state: {
        worknumber:'',
        privilege:'',
        header:'学院毕业综合成绩分析系统',
        faculties: [],
        students: [],
        grades:[],
        class:[],
        queue:[]
    },
    mutations:{
        storeUserInfo(state, newval) {
            state.worknumber = newval.worknumber
            state.privilege = newval.privilege
        },
        initData(state, newval) {
            newval.$http.get('/initData').then((res)=>{
                let list1 = []
                for(var index in res.data.faculties) {
                    list1.push(res.data.faculties[index])
                }
                state.faculties = list1

                let list2 = []
                for(var index in res.data.students) {
                    list2.push(res.data.students[index])
                }
                state.students = list2

                let list3 = []
                for(var index in res.data.grades) {
                    list3.push(res.data.grades[index])
                }
                state.grades = list3

                let list4 = []
                for(var index in res.data.class) {
                    list4.push(res.data.class[index])
                }
                state.class = list4

                let list5 = []
                for(var index in res.data.queue) {
                    list5.push(res.data.queue[index])
                }
                state.queue = list5

            }) 
        }
    }
})

export default store