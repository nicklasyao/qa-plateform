<template>
    <div class="container">
        <el-row>
            <el-col :span="16">
                <div class="form-box">
                    <el-form ref="form" :model="form" label-width="100px">
                        <el-form-item label="订单编号">
                            <el-input v-model="form.orderId" disabled></el-input>
                        </el-form-item>
                        <el-form-item label="操作人">
                            <el-input v-model="form.editUserId"></el-input>
                        </el-form-item>
                        <el-form-item label="销售顾问">
                            <el-input v-model="form.pointsale"></el-input>
                        </el-form-item>
                        <el-form-item label="销售顾问电话">
                            <el-input v-model="form.pointsalePhone"></el-input>
                        </el-form-item>
                        <el-form-item>
                            <el-button type="primary" @click="addPointSale">提交</el-button>
                        </el-form-item>
                    </el-form>
                </div>
            </el-col>
            <el-col :span="6">
                <pre>{{ result }}</pre>
            </el-col>
        </el-row>
    </div>
</template>

<script>
    // this.root.ORDERID = 'TEST'
    export default {
        name: "AddPointSale",
        data: function () {
            return {
                form: {
                    editUserId:
                        "2e8083b644394de9afb7ab30ae9e7ed6",
                    orderId: this.$root.ORDERID,
                        // "PLD0000000163",
                    pointsale:
                        "姚姚",
                    pointsalePhone:
                        "18820019144"
                },
                result: '{"msg":"此处显示请求的结果"}'
            }
        },
        methods: {
            addPointSale: function () {
                this.$axios({
                    method: 'POST',
                    url: '/data/pointsale/add',
                    data: this.form
                }).then((resp) => {
                    console.log(resp)
                    this.result = resp.data
                })
            }
        }
    }
</script>

<style scoped>

</style>
