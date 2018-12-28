<template>
    <div class="crumbs">
        <el-breadcrumb separator="||">
            <el-breadcrumb-item><i class="el-icon-lx-calendar"></i>进件管理</el-breadcrumb-item>
            <el-breadcrumb-item><router-link to="/house/add">登记房源</router-link></el-breadcrumb-item>
            <el-breadcrumb-item><router-link to="/pointsale/add">销售顾问</router-link></el-breadcrumb-item>
            <el-breadcrumb-item><router-link to="/bank/add">还款账户</router-link></el-breadcrumb-item>
            <el-breadcrumb-item><router-link to="/customer/add">添加客户</router-link></el-breadcrumb-item>
            <el-breadcrumb-item></el-breadcrumb-item>
        </el-breadcrumb>
        <router-view></router-view>
    </div>
</template>

<script>
    export default {
        name: "ApplyHome",
        data: function () {
            return {
            }
        },
        components: {
        }
    }
</script>

<style scoped>
    .is-active{
        color: #8cc5ff;
    }
</style>
