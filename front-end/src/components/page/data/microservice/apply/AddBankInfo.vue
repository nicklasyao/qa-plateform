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
                            <el-form-item label="银行卡户名">
                                <el-input v-model="form.accountName"></el-input>
                            </el-form-item>
                            <el-form-item label="身份证号码">
                                <el-input v-model="form.certId"></el-input>
                            </el-form-item>
                            <el-form-item label="还款银行卡号">
                                <el-input v-model="form.accountNo"></el-input>
                            </el-form-item>
                            <el-form-item label="银行卡预留手机号">
                                <el-input v-model="form.accountMobile"></el-input>
                            </el-form-item>
                            <el-form-item label="开户行">
                                <el-input v-model="form.repaymentBankNo"></el-input>
                            </el-form-item>
                            <el-form-item label="开户行所在省份">
                                <el-input v-model="form.branchBankProvince"></el-input>
                            </el-form-item>
                            <el-form-item label="开户行所在城市">
                                <el-input v-model="form.branchBankCity"></el-input>
                            </el-form-item>
                            <el-form-item label="开户行分行">
                                <el-input v-model="form.repaymentSubBankNo"></el-input>
                            </el-form-item>
                            <el-form-item label="开户行支行">
                                <el-input v-model="form.bankBranch"></el-input>
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
        name: "AddBankInfo",
        data: function () {
            return {
                form: {
                    editUserId:'2e8083b644394de9afb7ab30ae9e7ed6',
                    accountName:'姚姚',
                    certId:'441283199506184165',
                    accountNo:'6216617008000485728',
                    accountMobile:'15578955071',
                    repaymentBankNo:'C10104',
                    branchBankProvince:'110000',
                    branchBankCity:'110200',
                    repaymentSubBankNo:'北京',
                    bankBranch:'海淀',
                    serialNo:this.$root.ORDERID
                },
                result: '{"msg":"此处显示请求的结果"}'
            }
        },
        methods: {
            insert: function () {
                this.$axios({
                    method: 'POST',
                    url: '/data/payinfo/add',
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
