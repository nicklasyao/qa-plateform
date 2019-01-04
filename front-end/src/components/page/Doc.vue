<template>
    <div>
            <el-table :data="urls" style="width: 100%">
                <el-table-column prop="name" label="技术栈">
                </el-table-column>
                <el-table-column label="文档地址">
                    <template slot-scope="scope">
                        <a v-bind:href="scope.row.link" target="_blank">{{scope.row.link}}</a>
                    </template>
                </el-table-column>
            </el-table>
    </div>
</template>

<script>
    export default {
        name: "Doc",
        data() {
            return {
                urls: [
                    {name:'Python', link:'https://www.python.org/'},
                    {name:'Django', link:'https://www.djangoproject.com/'},
                    {name:'Django中文', link:'https://docs.djangoproject.com/zh-hans/2.1/'},
                    {name:'Django Suit', link:'https://django-suit.readthedocs.io/en/latest/configuration.html'},
                    {name:'Bootstrap', link:'http://www.bootcss.com/'},
                    {name:'Vue', link:'https://cn.vuejs.org/'},
                    {name:'ElementUI', link:'http://element-cn.eleme.io/#/zh-CN'},
                ]
            }
        }
    }
</script>

<style scoped>

</style>
