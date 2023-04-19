<template>
<div>
    <el-form v-show="isShow" :inline="true" :model="class_info" class="demo-form-inline">
        <el-form-item label="教学班序号">
            <el-input :disabled="disabled" v-model="class_info.class_id" placeholder="添加时无需填写"></el-input>
        </el-form-item>
        <el-form-item label="教学班年级">
            <el-input :disabled="!isAdd" v-model="class_info.grade" placeholder="年级"></el-input>
        </el-form-item>
        <el-form-item label="教学班名称">
            <el-input v-model="class_info.class_name" placeholder="学员队名称"></el-input>
        </el-form-item>
        <el-form-item label="教学班教员">
            <el-select v-model="class_info.tutor_id" placeholder="教员工号">
                <el-option v-for="(item, index) in this.$store.state.faculties" 
                :label="item.worknumber" :value="item.worknumber" :key="index"
                v-if="item.privilege == 'tutor'"></el-option>
            </el-select>
        </el-form-item>
        <el-form-item label="学员队">
            <el-select v-model="class_info.queue_id" placeholder="学员队名称">
                <el-option v-for="(item, index) in this.$store.state.queue" 
                :label="item.queue_name" :value="item.queue_id" :key="index"
                v-if="item.queue_grade == class_info.grade"></el-option>
            </el-select>
        </el-form-item>
    <el-form-item>
        <el-button type="primary" @click="enter()">确定</el-button>
        <el-button type="primary" @click="cancel()">取消</el-button>
    </el-form-item>
    </el-form>


  <el-table
    :data="this.$store.state.class"
    stripe
    style="width: 100%">
    <el-table-column prop="class_id" label="序号" width="200"></el-table-column>
    <el-table-column prop="class_name" label="班级名" width="200"></el-table-column>
    <el-table-column prop="grade" label="年级"></el-table-column>
    <el-table-column prop="queue_name" label="学员队"></el-table-column>
    <el-table-column prop="queue_id" label="学员队编号"></el-table-column>
    <el-table-column prop="tutor_name" label="教员"></el-table-column>
    <el-table-column prop="tutor_id" label="教员工号"></el-table-column>
    <el-table-column label="操作" align="center" min-width="100">
　　　　<template slot-scope="scope">
        <el-button type="primary" @click="changeClass(scope.row)">修改</el-button>
        <el-button type="primary" @click="deleteClass(scope.row)">删除</el-button>
　　　　</template>
　　</el-table-column>
    </el-table>
    <el-button type="primary" @click="addTab">添加学员队</el-button>
</div>
</template>

<script>
export default {
    name: 'ClassManage',
    data() {
        return{
            class_info: {
                class_id:'',
                class_name:'',
                grade:'',
                queue_id:'',
                tutor_id:''
            },
            isShow: false,
            isAdd: true,
            disabled:true,
            isfirst:false
        }
    },
    methods: {
        changeClass(e) {

            this.cancel()

            this.isfirst = true
            this.class_info.grade = e.grade
            this.isShow = true
            this.isAdd = false
            this.class_info.class_id = e.class_id
            this.class_info.class_name = e.class_name
            this.class_info.queue_id = e.queue_id
            this.class_info.tutor_id = e.tutor_id

            console.log(this.class_info)
        },
        deleteClass(e) {
            alert('暂时不能删除！')
        },
        addTab() {
            this.cancel()

            this.isShow = true
            this.isAdd = true
        },
        enter() {
            let path = ''
            if(this.isAdd) {
                path = '/add_class'
            }else {
                path = '/change_class'
            }

            if(this.class_info.class_name == '' |
            this.class_info.grade == '' |
            this.class_info.queue_id == '' |
            this.class_info.tutor_id == '' ) {
                alert('提交的数据不完整')
                return
            }

            this.$http.post(path, this.class_info).then((res)=>{
                if(res.data == 'ok') {
                    alert('操作成功！')
                    this.$store.commit('initData', this)
                    this.cancel()
                }else {
                    alert('已有相同班级名称，请修改后重试！')
                }
            })


        },
        cancel() {
            this.class_info.class_id = ''
            this.class_info.class_name = ''
            this.class_info.grade = ''
            this.class_info.queue_id = ''
            this.class_info.tutor_id = ''
            this.isShow = false
        }
    },
    watch: {
        'class_info.grade':function() {
            if(this.isfirst) {
                this.isfirst = false
            }else {
                this.class_info.queue_id = ''
            }
        }
    }
}
</script>

<style>

</style>