<template>
  <div id="Container">
    <div class = "admin-header">
        {{ this.head }}
    </div>
    <div>
            <el-button v-show="!isShow" @click="back">back</el-button>
    </div>
    <div v-show="isShow & this.$store.state.privilege != 'student'"  class="title" @click="navigate('gradesUpload')">
        <img src="@/assets/logo.png">
        <div>
            成绩录入
        </div>
    </div>
    <div v-show="isShow & this.$store.state.privilege != 'student' " class="title" @click="navigate('gradesManage')">
        <img src="@/assets/logo.png">
        <div>
            成绩查询
        </div>
    </div>
    <div v-show="isShow & this.$store.state.privilege == 'student'" class="title" @click="navigate('analyse')">
        <img src="@/assets/logo.png">
        <div>
            个人成绩分析
        </div>
    </div>
    <router-view style="width: 100%;height: 100%;"></router-view>
    </div>
</template>

<script>
export default {
    name:'ControlTab',
    data() {
        return {
            head: '学生毕业综合成绩数据分析系统',
            isShow: true
        }
    },
    methods:{
        navigate(index) {
            this.isShow = !this.isShow
            this.$router.push('/controlTab/' + index)
        },
        back() {
            this.$router.go(-1)
        }
    },
    watch: {
        '$route': function(to, from) {
            if(to.path == '/controlTab') {
                this.isShow = true
            }
        }
    },
    created() {
        console.log(this.$store.state.privilege)
        if(this.$store.state.privilege == 'cadre') {
            this.head += '(干部)'
        }else if(this.$store.state.privilege == 'tutor') {
            this.head += '(教员)'
        }else {
            this.head += '(学生)'
        }
    }
}
</script>

<style>
#Container {
    width: 100%;
    height: 100%;
}

.title {
    text-align: center;
    width: 30%;
    margin-left: 5px;
    float: left;
}

.admin-header {
    background-color: #1C584E;
    color: white;
    height:120px;
    text-align: center;
    line-height: 120px;
    font-size: 30px;
}
</style>