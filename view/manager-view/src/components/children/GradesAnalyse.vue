<template>
  <div style="width: 100%; height: 100%;">
    <div style="width:100%; height:400px">
        <div id="rader" style="width:50%; height: 100%; float: right;" ref="a1"></div>
        <div style="width:50%; height: 100%; " ref="a2"></div>
    </div>
    <el-table
      :data="this.table_data"
      style="width: 100%">
      <el-table-column
        prop="name"
        label="科目"
        width="250">
      </el-table-column>
      <el-table-column
        prop="grades"
        label="成绩"
        width="250">
      </el-table-column>
      <el-table-column
        prop="rank"
        label="排名">
      </el-table-column>
      <el-table-column label="操作" align="center" min-width="100">
        <template slot-scope="scope">
        <el-popover
            placement="right"
            width="400"
            trigger="click">
            <el-table :data="getDetail(scope.row.link)">
                <el-table-column width="150" property="time" label="学年"></el-table-column>
                <el-table-column width="150" property="grades" label="成绩"></el-table-column>
            </el-table>
            <el-button slot="reference" 
            v-if="scope.row.name != '总成绩'" 
            type="primary">查看详情</el-button>
        </el-popover>
        </template>
　　    </el-table-column>
    </el-table>
  </div>
</template>

<script>

export default {
    name: 'GradesAnalyse',
    data() {
        return {
            analyse_data: [],
            line_data:{
                category:[],
            },
            radar_data:[],
            isWait: true,
            table_data:[],
            org_detail:[],
            exam_detail:[],
            second_detail:[],
            study_detail:[]
        }
    },
    created() {
        
    },
    mounted() {
        this.$http.post('/grades_analyse', {'sid':this.$store.state.worknumber}).then((res)=>{
            this.analyse_data = res.data
            // 生成横坐标
            var grade = this.analyse_data.grade
            for(var i=0; i<4, i++;) {
                this.line_data.category.push(grade+i)
            }
            console.log(this.analyse_data)
           this.drawA1()
           this.drawA2()

           // 处理数据用于表格显示
           let org = {
            grades: this.analyse_data.org.score,
            name: this.analyse_data.org.name,
            rank: this.analyse_data.org.rank,
            link: 'org_detail'
           } 
           this.table_data.push(org)

           let study = {
            grades: this.analyse_data.study.score,
            name: this.analyse_data.study.name,
            rank: this.analyse_data.study.rank,
            link: 'study_detail'
           } 
           this.table_data.push(study)

           let second = {
            grades: this.analyse_data.second.score,
            name: this.analyse_data.second.name,
            rank: this.analyse_data.second.rank,
            link: 'second_detail'
           } 
           this.table_data.push(second)

           let exam = {
            grades: this.analyse_data.exam.score,
            name: this.analyse_data.exam.name,
            rank: this.analyse_data.exam.rank,
            link: 'exam_detail'
           } 
           this.table_data.push(exam)

           let total = {
            grades: this.analyse_data.total.score,
            name: this.analyse_data.total.name,
            rank: this.analyse_data.total.rank,
            link: 'total'
           } 
           this.table_data.push(total)

           // 处理详情预览页的数据
           for(var key in this.analyse_data.org) {
            if(key != 'rank' && key != 'score' && key != 'avg' && key != 'name') {
                this.org_detail.push(this.analyse_data.org[key])
            }
           }
           for(var key in this.analyse_data.study) {
            if(key != 'rank' && key != 'score' && key != 'avg' && key != 'name') {
                this.study_detail.push(this.analyse_data.study[key])
            }
           }
           for(var key in this.analyse_data.exam) {
            if(key != 'rank' && key != 'score' && key != 'avg' && key != 'name') {
                this.exam_detail.push(this.analyse_data.exam[key])
            }
           }
           for(var key in this.analyse_data.second) {
            if(key != 'rank' && key != 'score' && key != 'avg' && key != 'name') {
                this.second_detail.push(this.analyse_data.second[key])
            }
           }
           
        })
    },
    methods: {
        drawA1() {
            let myChart = this.$echarts.init(this.$refs.a1)

            // 填充雷达图数据
            let radar_data = []

            let avg = []
            avg.push(this.analyse_data.total.avg)
            avg.push(this.analyse_data.study.avg)
            avg.push(this.analyse_data.org.avg)
            avg.push(this.analyse_data.second.avg)
            avg.push(this.analyse_data.exam.avg)

            radar_data.push({name: '平均分数', value: avg})


            let personel = []
            personel.push(this.analyse_data.total.score)
            personel.push(this.analyse_data.study.score)
            personel.push(this.analyse_data.org.score)
            personel.push(this.analyse_data.second.score)
            personel.push(this.analyse_data.exam.score)

           radar_data.push({name: '个人分数', value: personel})
           
           this.radar_data = radar_data

            let option = {
                title: {
                    text: '个人能力图'
                },
            legend: {
                data: ['平均分数', '个人分数']
            },
            radar: {
                // shape: 'circle',
                indicator: [
                { name: '总分数', max: 100 },
                { name: '学习成绩', max: 100},
                { name: '组织评价', max: 100 },
                { name: '第二课堂', max: 100 },
                { name: '联考成绩', max: 100 },
                ]
            },
            series: [
                {
                    type: 'radar',
                    data: this.radar_data
                }
            ]
            }
            myChart.setOption(option)
        },
        drawA2() {
            let myChart = this.$echarts.init(this.$refs.a2)
            let option = {
            tooltip: {
                trigger: 'axis'
            },
            legend: {
                data: ['学习成绩', '组织评价', '第二课堂', '联考成绩']
            },
            grid: {
                left: '3%',
                right: '4%',
                bottom: '3%',
                containLabel: true
            },
            toolbox: {
                feature: {
                    saveAsImage: {}
                }
            },
            xAxis: {
                type: 'category',
                boundaryGap: false,
                data: []
            },
            yAxis: {
                type: 'value'
            },
            series: [
            ]
            }
            let grade = this.analyse_data.grade
            // 组装横坐标
            for(var i=0; i<4; i++) {
                option.xAxis.data.push(grade ++)
            }
            // 组装各项成绩
            
            let serie1 = {
                name:'',
                type: 'line',
                stack: 'Total',
                data:[]
            }
            serie1.name = "学习成绩"
            for(var key in this.analyse_data.study) {
                if(key != 'score' && key != 'avg' && key !='rank' && key != 'name') {
                    serie1.data.push(this.analyse_data.study[key].grades)
                }
            }
            option.series.push(serie1)



            let serie2 = {
                name:'',
                type: 'line',
                stack: 'Total',
                data:[]

            }
            serie2.name = "组织评价"
            for(var key in this.analyse_data.org) {
                if(key != 'score' && key != 'avg' && key !='rank') {
                    serie2.data.push(this.analyse_data.org[key].grades)
                }
            }
            option.series.push(serie2)



            let serie3 = {
                name:'',
                type: 'line',
                stack: 'Total',
                data:[]
            }
            serie3.name = "第二课堂"
            for(var key in this.analyse_data.second) {
                if(key != 'score' && key != 'avg' && key !='rank') {
                    serie3.data.push(this.analyse_data.second[key].grades)
                }
            }
            option.series.push(serie3)


            
            let serie4 = {
                name:'',
                type: 'line',
                stack: 'Total',
                data:[]
            }
            serie4.name = "联考成绩"
            for(var key in this.analyse_data.exam) {
                if(key != 'score' && key != 'avg' && key !='rank') {
                    serie4.data.push(this.analyse_data.exam[key].grades)
                }
            }
            option.series.push(serie4)


            myChart.setOption(option)
        },
        getDetail(e) {
            if(e == 'org_detail') {
                return this.org_detail
            }else if (e == 'study_detail') {
                return this.study_detail
            }else if (e == 'exam_detail') {
                return this.exam_detail
            } else {
                return this.second_detail
            }
        }
    }
}
</script>

<style>

</style>