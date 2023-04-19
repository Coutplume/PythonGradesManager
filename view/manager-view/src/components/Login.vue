<template>
  <div id="loginContainer">

    <div id="loginDiv">
      <div id="header">
        学生毕业综合成绩数据分析系统
      </div>
          <div><input class="in1" v-model="username" placeholder="请输入账号"></div>
          <div><input class="in1" v-model="password" placeholder="请输入密码"></div>
          <div style="text-align: right; padding-right: 10%; padding-top: 20px;"><input type="radio" v-model="type" value="faculty">教职工<input type="radio" v-model="type" value="student">学生</div>
          <el-button style="width: 80%; font-size:25px" @click="login">登录</el-button>
    </div>
  </div>
</template>

<script>
export default {
    name:'Login',
    data() {
        return {
            username: 'DSB123',
            password: '1',
            type: 'faculty'
        }
    },
    methods: {
      login(){
        let data = {
            worknumber: this.username,
            password: this.password
          }

        if(this.type == "faculty") {
          this.$http.post('/faculty_login',data).then((res)=>{
            if(res.data.status == 'ok') {
              let userInfo = {
                privilege: res.data.privilege,
                worknumber: res.data.worknumber
              }
              this.$store.commit('storeUserInfo', userInfo)
              this.$store.commit('initData', this)

              if (userInfo.privilege == 'admin'){
                this.$router.push('/admin')
              }else {
                this.$router.push('/controlTab')
              }
            }
          })
        }else {
          this.$http.post('/student_login',data).then((res)=>{
            if(res.data.status == 'ok') {
              let userInfo = {
                privilege: res.data.privilege,
                worknumber: res.data.sid
              }
              this.$store.commit('storeUserInfo', userInfo)
              this.$store.commit('initData', this)

              if (userInfo.privilege == 'admin'){
                this.$router.push('/admin')
              }else {
                this.$router.push('/controlTab')
              }
            }
          })
        }
      }
    }
}
</script>

<style>
#loginDiv {
  margin-right: 10%;
  margin-left: 60%;
  width: 30%;
  text-align: center;
  background-color: white;
  height: 60%;
  padding-top: 20px;
}

#loginContainer {
  width: 100%;
  height:100%;
  padding-top: 10%;
  background-image: url('../assets/login.jpg');
  background-repeat: no-repeat;
  background-size: cover;
  background-position: center;
}

.in1 {
  margin-top: 20px;
  width: 80%;
  height: 50px;
  box-sizing: border-box;
  font-size: 20px;
}

#header {
  width: 110%;
  height: 50px;
  line-height: 50px;
  font-size: 30px;
  font-family: 	SimHei;
  background-color: #1C584E;
  color: aliceblue;
  text-align: left;
  padding-left: 5px;
  margin-left: -15%;
}
</style>