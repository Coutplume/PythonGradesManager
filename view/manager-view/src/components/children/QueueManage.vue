<template>
    <div>
    <el-form v-show="isShow" :inline="true" :model="queue_info" class="demo-form-inline">
        <el-form-item label="学员队序号">
            <el-input :disabled="disabled" v-model="queue_info.queue_id" placeholder="添加时无需填写"></el-input>
        </el-form-item>
        <el-form-item label="学员队年级">
            <el-input v-model="queue_info.queue_grade" placeholder="年级"></el-input>
        </el-form-item>
        <el-form-item label="学员队名称">
            <el-input v-model="queue_info.queue_name" placeholder="学员队名称"></el-input>
        </el-form-item>
        <el-form-item label="学员队干部">
            <el-select v-model="queue_info.queue_cadre" placeholder="干部工号">
                <el-option v-for="(item, index) in this.$store.state.faculties" 
                :label="item.worknumber" :value="item.worknumber" :key="index"
                v-if="item.privilege == 'cadre'"></el-option>
            </el-select>
        </el-form-item>
    <el-form-item>
        <el-button type="primary" @click="enter()">确定</el-button>
        <el-button type="primary" @click="cancel()">取消</el-button>
    </el-form-item>
    </el-form>

    <el-table
    :data="this.$store.state.queue"
    stripe
    style="width: 100%">
    <el-table-column prop="queue_id" label="序号" width="200"></el-table-column>
    <el-table-column prop="queue_name" label="队名" width="200"></el-table-column>
    <el-table-column prop="queue_grade" label="年级"></el-table-column>
    <el-table-column prop="cadre_name" label="干部"></el-table-column>
    <el-table-column prop="queue_cadre" label="干部工号"></el-table-column>
    <el-table-column label="操作" align="center" min-width="100">
　　　　<template slot-scope="scope">
        <el-button type="primary" @click="changeQueue(scope.row)">修改</el-button>
        <el-button type="primary" @click="deleteQueue(scope.row)">删除</el-button>
　　　　</template>
　　</el-table-column>
    </el-table>
    <el-button type="primary" @click="addTab">添加学员队</el-button>
    </div>
</template>

<script>
export default {
    name: 'QueueManage',
    data() {
        return {
            queue_info:{
                queue_id:'',
                queue_name:'',
                queue_grade:'',
                cadre_name:'',
                queue_cadre:''
            },
            isShow: false,     
            // 判断是添加还是修改
            flag:true,
            disabled: true
        }
    },
    methods: {
        changeQueue(e) {
            this.queue_info.queue_id = e.queue_id
            this.queue_info.queue_grade = e.queue_grade
            this.queue_info.queue_name = e.queue_name
            this.queue_info.queue_cadre = e.queue_cadre
            this.isShow = true
            this.flag = false
        },
        deleteQueue(e) {
            alert('暂时不支持取消')
        },
        cancel() {
            this.queue_info.queue_id = ''
            this.queue_info.queue_grade = ''
            this.queue_info.queue_name = ''
            this.queue_info.queue_cadre = ''
            this.queue_info.cadre_name  = ''
            this.isShow = false
        },
        addTab() {
            this.cancel()
            this.isShow = true
            this.flag = true
        },
        enter() {

            if( this.queue_info.queue_grade == '' ||
                this.queue_info.queue_name == ''  ||
                this.queue_info.queue_cadre == '' ) {
                    alert('数据不完整！')
                    return
                }

            let path = ''
            if(this.flag) {
                // 添加
                path = '/add_queue'
            }else {
                // 修改
                path = '/change_queue'
            }

            this.$http.post(path, this.queue_info).then((res)=>{
                    if(res.data == 'ok') {
                        alert('操作成功！')
                        this.$store.commit('initData', this)
                        this.cancel()
                    }else {
                        alert('已存在相同的队列,请重试')
                    }
                })
        }
    }
}
</script>

<style>

</style>