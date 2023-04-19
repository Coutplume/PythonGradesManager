<template>
  <div style="width: 100%; height: 100%; text-align: center;">
    <el-form :inline="true" :model="grades" class="demo-form-inline">
    <el-form-item label="成绩类型">
        <el-select v-model="grades.type" placeholder="请选择...">
            <el-option label="组织评价" value="org"></el-option>
            <el-option label="学习成绩" value="study"></el-option>
            <el-option label="第二课堂" value="second"></el-option>
            <el-option label="联考成绩" value="exam"></el-option>
        </el-select>
    </el-form-item>
    <el-form-item>
        <el-upload
        :on-change="addFile"
        accept=".xlsx"
        action="">
        <el-button size="small" type="primary">点击上传</el-button>
        </el-upload>
    </el-form-item>
    </el-form>
  </div>
</template>

<script>
export default {
    name: 'GradesUpload',
    data() {
        return {
            grades: {
                type: '',
                file: ''
            },
            isUploaded: false
        }
    },
    methods: {
        addFile(e) {
            if(this.isUploaded) {
                this.isUploaded = !this.isUploaded
            }else {
                this.isUploaded = !this.isUploaded
                return
            }

            if(this.grades.type == '') {
                alert('请先选择类型！')
                return
            }

            let reader = new FileReader()
            reader.readAsDataURL(e.raw)
            reader.onload = (e)=>{
                this.grades.file = e.target.result;
                this.$http.post('upload_grades', this.grades).then((res)=>{
                    this.$store.commit('initData',this)
                    if(res.data.errNum != 0) {
                        alert(res.data.errNum + '条数据添加失败！')
                    }else {
                        alert('添加成功!')
                    }
                })
        }
        }
    }
}
</script>

<style>

</style>