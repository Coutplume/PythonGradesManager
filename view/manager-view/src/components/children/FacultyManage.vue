<template>
  <div>
    <div>
    <el-form v-show="isShow" label-position="right" label-width="80px" :model="UserInfo">
        <el-form-item label="工号"><el-input :disabled="flag" v-model="UserInfo.worknumber"></el-input></el-form-item>
        <el-form-item label="姓名"><el-input v-model="UserInfo.name"></el-input></el-form-item>
        <el-form-item label="密码"><el-input v-model="UserInfo.password"></el-input></el-form-item>
        <el-form-item label="职位">
            <el-select v-model="UserInfo.privilege" placeholder="请选择">
                <el-option label="管理员" value="admin"></el-option>
                <el-option label="教员" value="tutor"></el-option>
                <el-option label="干部" value="cadre"></el-option>
            </el-select>
        </el-form-item>    
        <el-form-item>
            <el-button type="primary" @click="enter">确定</el-button>
            <el-button type="primary" @click="cancel">取消</el-button>
        </el-form-item>
    </el-form>
    </div>

    <el-table
    :data="this.$store.state.faculties"
    stripe
    style="width: 100%">
    <el-table-column prop="worknumber" label="工号" width="200"></el-table-column>
    <el-table-column prop="name" label="姓名" width="200"></el-table-column>
    <el-table-column prop="privilege" label="职位"></el-table-column>
    <el-table-column label="操作" align="center" min-width="100">
　　　　<template slot-scope="scope">
        <el-button type="primary" @click="changeUser(scope.row)">修改</el-button>
        <el-button type="primary" @click="deleteUser(scope.row)">删除</el-button>
　　　　</template>
　　</el-table-column>
    </el-table>
    <el-button type="primary" @click="addTab">添加用户</el-button>
       
  </div>
</template>

<script>
export default {
    name: 'FacultyManage',
    data() {
        return {
            UserInfo: {
                worknumber:'',
                name: '',
                password: '',
                privilege: ''
            },
            isShow : false,
            flag : false,
            option:''
        }
    },
    created() {
        console.log(this.$store.state.faculties)
    },
    methods: {
        deleteUser(val) {
            if(val.privilege == 'admin') {
                alert('用户为管理员！无法删除！')
            }
            this.$http.post('/delete_user', {'worknumber' : val.worknumber}).then((res)=>{
                if(res.data == 'ok') {
                    alert('删除成功！')
                    this.$store.commit('initData', this)
                }
            })
        },
        changeUser(val) {
            this.cancel()

            this.UserInfo.name = val.name
            this.UserInfo.worknumber = val.worknumber
            this.UserInfo.password = val.password
            this.UserInfo.privilege = val.privilege
            this.isShow = true
            this.flag = true
            this.option = 'changeUser'
        },
        cancel() {
            this.UserInfo.name = ''
            this.UserInfo.worknumber = ''
            this.UserInfo.password = ''
            this.UserInfo.privilege = ''
            this.isShow = false
            this.flag = false
        },
        change() {
            console.log(this.UserInfo)
            this.$http.post('/change_user_info', this.UserInfo).then((res)=>{
                if(res.data == 'ok') {
                    this.$store.commit('initData', this)
                    this.cancel()
                }
            })
        },
        addTab() {
            this.cancel()

            this.isShow = true
            this.option = 'addUser'
        },
        enter() {
            if(this.option == 'changeUser') {
                this.change()
            }else {
                this.add()
            }
        },
        add() {
            if(this.UserInfo.worknumber == '' || this.UserInfo.name == '') {
                alert('不能为空！')
                return
            }
            this.$http.post('/add_faculty', this.UserInfo).then((res)=>{
                if(res.data == 'error') {
                    alert("工号已存在，请更换后重试")
                    this.UserInfo.worknumber = ''
                }else {
                    alert("添加成功！")
                    this.$store.commit('initData', this)
                    this.cancel()
                }
            })
        }
    }
}
</script>

<style>

</style>