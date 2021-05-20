<template>
  <!-- hidden PageHeaderWrapper title demo -->
  <page-header-wrapper :title="false" :content="$t('form.basic-form.basic.description')">
    <a-card :body-style="{padding: '24px 32px'}" :bordered="false">
      <a-form :form="form">
        <a-form-item
          :label="$t('请输入您要发送的消息')"
          :labelCol="{lg: {span: 7}, sm: {span: 7}}"
          :wrapperCol="{lg: {span: 10}, sm: {span: 17} }">
          <a-textarea
            rows="2"
            :placeholder="$t('form.basic-form.standard.placeholder')"
            v-decorator="[
              'type',
              {rules: [{ required: true, message: $t('form.basic-form.standard.required') }]}
            ]" />
        </a-form-item>

        <a-form-item :wrapperCol="{ span: 24 }" style="text-align: center">
          <a-button type="primary" @click="showModal">
          Send
          </a-button>
          <a-modal v-model="visible" title="ECMP Automatic Response" @ok="handleOk">
          <p>{{resp}}</p>
          </a-modal>
        </a-form-item>
      </a-form>
    </a-card>
  </page-header-wrapper>
</template>

<script>
export default {
  name: 'BaseForm',
  data () {
    return {
      form: this.$form.createForm(this)
    }
  },
  methods: {
    // handler
    handleSubmit (e) {
      e.preventDefault()
      this.form.validateFields((err, values) => {
        if (!err) {
          console.log('Received values of form: ', values)
        }
      })
    }
  }
}
</script>

<script>
export default {
  name: 'BaseForm',
  data() {
    return {
      form: this.$form.createForm(this),
      visible: false,
      resp: "",
    };
  },
  methods: {
    showModal() {
      let req = {"query":"今天天气真好"};
      this.form.validateFields((err, values) => {
        req = {"query":values.type}
        console.log(req);
      });
      console.log(req);
      this.visible = true;
      this.axios.post('/ecmp/chat',req).then((response)=>{
        this.resp=response.result;
      }).catch((response)=>{
        console.log(response);
      });
    },
    handleOk(e) {
      console.log(e);
      this.visible = false;
    },
  },
};
</script>
