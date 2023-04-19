<template>
  <div id="app">
    <transition name="fade" mode="out-in">
      <router-view />
    </transition>
    <!-- <input @change="addFile($event)"
    type="file"
    accept=".xlsx"> -->
  </div>
</template>

<script>
export default {
  name: 'App',
  created() {
  },
  methods: {
    addFile(e) {
      let reader = new FileReader()
      reader.onload = (e)=>{
        //console.log(e.target.result)
        let data = {'data':e.target.result};
        this.$http.post('add_student',data).then((res)=>{
          console.log(res.data)
        })
      }
      reader.readAsDataURL(e.target.files[0])

    }
  }
}
</script>

<style>
#app {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  width: 100%;
  height: 100%;
}

.fade-enter {
  opacity: 0;
  transform: translateX(100%);
  padding: 0px;
}
.fade-leave-to {
  opacity: 1;
  transform: translateX(-100%);
  /**该position属性使其脱离文档流 ，不会占位*/
  /**但是脱离文档流会造成页面大小未知的变形，所以最好不适用 
    position: absolute;
    更推荐使用mode: out-in
  */
}
.fade-enter-active, 
.fade-leave-active {
  transition:all .2s ease;
}

html, body {
  height: 100%;
  padding:0; margin:0;
}


</style>
