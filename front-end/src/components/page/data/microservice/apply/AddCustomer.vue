<template>
    <div class="wrapper">
        <div class="container">
            <el-row>
                <el-col :span="16">
                    <div class="form-box">
                        <el-form ref="form" :model="form" label-width="150px">
                            <el-form-item label="订单编号">
                                <el-input v-model="form.serialNo" disabled></el-input>
                            </el-form-item>
                            <el-form-item label="操作人">
                                <el-input v-model="form.editUserId"></el-input>
                            </el-form-item>
                            <el-form-item label="姓名">
                                <el-input v-model="form.customerName"></el-input>
                            </el-form-item>
                            <el-form-item label="身份证号码">
                                <el-input v-model="form.certId"></el-input>
                            </el-form-item>
                            <el-form-item>
                                <el-button type="primary" @click="insert">提交</el-button>
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
        name: "AddCustomerInfo",
        data: function () {
            return {
                form: {
                    editUserId: '2e8083b644394de9afb7ab30ae9e7ed6',
                    customerName: '姚献伟',
                    certId: '450802198612113150',
                    serialNo: this.$root.ORDERID
                },
                result: '{"msg":"此处显示请求的结果"}'
            }
        },
        methods:
            {
                insert: function () {
                    this.$axios({
                        method: 'POST',
                        url: '/data/customer/add',
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
