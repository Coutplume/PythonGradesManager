<template>
  <div style="height: 100%;">
    <div class = "admin-header">
        学生毕业综合成绩数据分析系统
    </div>
    <div>
        <el-button v-show="!isShow" @click="back">back</el-button>
    </div>
    <div v-show="isShow" class="title" @click="navigate('studentManage')">
        <img src="@/assets/logo.png">
        <div>
            学员管理
        </div>
    </div>
    <div v-show="isShow" class="title" @click="navigate('classManage')">
        <img src="@/assets/logo.png">
        <div>
            教学班管理
        </div>
    </div>
    <div v-show="isShow" class="title" @click="navigate('facultyManage')">
        <img src="@/assets/logo.png">
        <div>
            教职工管理
        </div>
    </div>
    <div v-show="isShow" class="title" @click="navigate('queueManage')">
        <img src="@/assets/logo.png">
        <div>
            学员队管理
        </div>
    </div>
    <router-view style="width: 100%;height: auto;">

    </router-view>
  </div>
</template>

<script>
export default {
    name: 'Admin',
    data() {
        return {
            isShow : true
        }
    },
    methods: {
        navigate(index) {
            this.isShow = !this.isShow
            this.$router.push('/admin/' + index)
        },
        back() {
            this.$router.go(-1)
        }
    },
    watch: {
        '$route': function(to, from) {
            if(to.path == '/admin') {
                this.isShow = true
            }
        }
    }
}
</script>

<style>
.title {
    text-align: center;
    width: 30%;
    height: 40%;
    margin-left: 3%;
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