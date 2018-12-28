<template>
    <div class="wrapper">
        <!--<apply-home></apply-home>-->
        <div class="container">
            <!--<el-row>-->
                <!--<div class="form-box">-->
                    <!--<h2>登记房源-->
                        <!--<small>修改保存房源登记信息</small>-->
                    <!--</h2>-->
                <!--</div>-->
            <!--</el-row>-->
            <el-row>
                <el-col :span="16">
                    <div class="form-box">

                        <el-form ref="form" :model="form" label-width="100px">
                            <el-form-item label="操作人">
                                <el-input v-model="form.editUserId"></el-input>
                            </el-form-item>
                            <el-form-item label="房间代码">
                                <el-input v-model="form.roomId"></el-input>
                            </el-form-item>
                            <el-form-item label="项目代码">
                                <el-input v-model="form.projectId"></el-input>
                            </el-form-item>
                            <el-form-item label="认筹号">
                                <el-input v-model="form.raiseNo"></el-input>
                            </el-form-item>
                            <el-form-item label="申请分期金额">
                                <el-input v-model="form.applyAmount"></el-input>
                            </el-form-item>
                            <el-form-item label="产品编号">
                                <el-input v-model="form.productCode"></el-input>
                            </el-form-item>
                            <el-form-item label="产品id">
                                <el-input v-model="form.productId"></el-input>
                            </el-form-item>
                            <el-form-item>
                                <el-button type="primary" @click="addHouse">提交</el-button>
                            </el-form-item>
                        </el-form>
                    </div>
                </el-col>
                <el-col :span="6">
                    <pre>{{ result }}</pre>
                </el-col>
            </el-row>
        </div>
    </div>
</template>

<script>
    export default {
        name: "AddHouse",
        data: function () {
            return {
                form: {
                    applyAmount: 1000000,
                    editUserId:
                        "2e8083b644394de9afb7ab30ae9e7ed6",
                    productCode:
                        "0000008",
                    productId:
                        "eb50229225824aa89562ffd6a5d0feb9",
                    projectId:
                        "yanshou",
                    raiseNo:
                        "raiseNo",
                    roomId:
                        "roomId"
                },
                result: '{"msg":"此处显示请求的结果"}'
            }
        },
        methods: {
            addHouse: function () {
                this.$axios({
                    method: 'POST',
                    url: '/data/house/add',
                    data: this.form
                }).then((resp) => {
                    console.log(resp)
                    this.result = resp.data
                    if (resp.data.data.result) {
                        this.$root.ORDERID = resp.data.data.result.serialNo
                    }
                })
            }
        }
    }
</script>

<style scoped>

</style>
