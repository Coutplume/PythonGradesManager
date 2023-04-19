<template>
  <div style="text-align: center;">
    <el-upload
    :on-change="addFile"
    accept=".xlsx"
    action="">
        <el-button size="small" type="primary">点击上传</el-button>
    </el-upload>
    <el-table
    :data="this.$store.state.students.slice((currentPage-1)*pageSize,currentPage*pageSize)"
    stripe
    style="width: 100%">
    <el-table-column prop="sid" label="序号"></el-table-column>
    <el-table-column prop="sno" label="学号" width="200"></el-table-column>
    <el-table-column prop="sname" label="姓名" width="200"></el-table-column>
    <el-table-column prop="class" label="教学班"></el-table-column>
    <el-table-column prop="queue" label="学员队"></el-table-column>
    <el-table-column prop="grade" label="年级"></el-table-column>
    <el-table-column label="操作" align="center" min-width="100">
　　　　<template slot-scope="scope">
        <el-button type="primary" @click="changeUser(scope.row)">修改</el-button>
        <el-button type="primary" @click="deleteUser(scope.row)">删除</el-button>
　　　　</template>
　　</el-table-column>
    </el-table>
    <el-pagination align='center' 
            @size-change="handleSizeChange" 
            @current-change="handleCurrentChange"
            :current-page="currentPage" 
            :page-sizes="[1,5,10,20]" 
            :page-size="pageSize" 
            layout="total, prev, pager, next, jumper" 
            :total="this.$store.state.students.length">
        </el-pagination>
  </div>
</template>

<script>
export default {
    name: 'StudentManage',
    data() {
        return {
            isUploaded: false,
            currentPage: 1, // 当前页码
            total: 20, // 总条数
            pageSize: 7 // 每页的数据条数
        }
    },
    methods: {
        addStudent() {

        },
        addFile(e) {
            if(this.isUploaded) {
                this.isUploaded = !this.isUploaded
            }else {
                this.isUploaded = !this.isUploaded
                return
            }
            let reader = new FileReader()
            reader.readAsDataURL(e.raw)
            reader.onload = (e)=>{
                let data = {'data':e.target.result};
                this.$http.post('add_student',data).then((res)=>{
                    if(res.data.status == 'error') {
                        alert(res.data.errNum + "条数据添加失败！")
                        return
                    }
                    this.$store.commit('initData',this)
                })
        }
        },
        //每页条数改变时触发 选择一页显示多少行
        handleSizeChange(val) {
            console.log(`每页 ${val} 条`);
            this.currentPage = 1;
            this.pageSize = val;
        },
        //当前页改变时触发 跳转其他页
        handleCurrentChange(val) {
            console.log(`当前页: ${val}`);
            this.currentPage = val;
        }
    }
}
</script>

<style>

</style>