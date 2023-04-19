<template>
    <div>
        <el-form :inline="true" :model="query_message" class="demo-form-inline">
            <el-form-item label="成绩类型">
                <el-select v-model="query_message.type">
                    <el-option label="全部" value="all"></el-option>
                    <el-option label="组织评价" value="org"></el-option>
                    <el-option label="学习成绩" value="study"></el-option>
                    <el-option label="第二课堂" value="second"></el-option>
                    <el-option label="联考成绩" value="exam"></el-option>
                </el-select>
            </el-form-item>
            <el-form-item label="教学班">
                <el-input v-model="query_message.class" placeholder="输入要查询的教学班"></el-input>
            </el-form-item>
            <el-form-item label="年级">
                <el-input v-model="query_message.grade" placeholder="输入的待查询班级的年级"></el-input>
            </el-form-item>
            <el-form-item>
                <el-button type="primary" @click="search">查询</el-button>
            </el-form-item>
        </el-form>
        <el-table
        :data="this.show_data.slice((currentPage-1)*pageSize,currentPage*pageSize)"
        stripe
        style="width: 100%">
        <el-table-column prop="grades_id" label="序号"></el-table-column>
        <el-table-column prop="sno" label="学号"></el-table-column>
        <el-table-column prop="sname" label="姓名"></el-table-column>
        <el-table-column prop="class" label="教学班"></el-table-column>
        <el-table-column prop="queue" label="学员队"></el-table-column>
        <el-table-column prop="grade" label="入学年份"></el-table-column>
        <el-table-column prop="time" label="学年"></el-table-column>
        <el-table-column prop="type_name" label="成绩类型"></el-table-column>
        <el-table-column prop="grades" label="成绩"></el-table-column>
        </el-table>
        <el-pagination align='center' 
            @size-change="handleSizeChange" 
            @current-change="handleCurrentChange"
            :current-page="currentPage" 
            :page-sizes="[1,5,10,20]" 
            :page-size="pageSize" 
            layout="total, prev, pager, next, jumper" 
            :total="show_data.length">
        </el-pagination>
    </div>
</template>

<script>
export default {
    name: 'GradesManage',
    data() {
        return {
            query_message: {
                type: 'all',
                class: '',
                grade: ''
            },
            show_data:[],
            currentPage: 1, // 当前页码
            total: 20, // 总条数
            pageSize: 8 // 每页的数据条数
        }
    },
    created() {
        this.show_data = this.$store.state.grades
    },
    methods: {
        search() {
            let list = this.$store.state.grades
            if(this.query_message.class == '' && this.query_message.grade == ''){
                if(this.query_message.type == 'all') {
                    this.show_data = list
                }else {
                    this.change_show_data(this.query_message.type)
                }
                this.currentPage = 1
            }else if(this.query_message.class == '' || this.query_message.grade == ''){
                alert('必须输入完整数据才能查询！')
                return
            }else {
                this.show_data = []
                if(this.query_message.type == 'all') {
                    for(var ele of list) {
                    if (ele.class == this.query_message.class && 
                    ele.time == this.query_message.grade){
                        this.show_data.push(ele)
                    }
                    }
                }else {
                    for(var ele of list) {
                    if (ele.class == this.query_message.class && 
                    ele.time == this.query_message.grade &&
                    ele.type == this.query_message.type){
                        this.show_data.push(ele)
                    }
                    }
                }

            }
        },
        change_show_data(type) {
            let list = this.$store.state.grades
            this.show_data = []
            for(var ele of list) {
                if(ele.type == type) {
                    this.show_data.push(ele)
                }
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