<template lang="pug">
  q-page(class="column wrap justify-center items-start content-center")
    div(style="width: 30%;")
      q-select(
        label="Entre com os valores"
        v-model="nrApples"
        use-input
        use-chips
        multiple
        hide-dropdown-icon
        input-debounce="0"
        bottom-slots
        new-value-mode="add")
        template(v-slot:before)
          q-avatar(size="60px")
            img(src="~assets/Apple.svg")
      div.row
        q-input(v-model="K" filled label="K" type="number" style="width: 120px")
          template(v-slot:before)
            q-avatar(size="60px")
              img(src="~assets/Farm.svg")
        q-input(v-model="L" filled label="L" type="number" style="width: 120px")
          template(v-slot:before)
            q-avatar(size="60px")
              img(src="~assets/Farmer.svg")
      q-btn(@click="calculate" style="margin: 20px;") Enviar
</template>

<script>
import { mapActions } from 'vuex'
export default {
  name: 'PageIndex',
  data () {
    return {
      nrApples: null,
      K: 0,
      L: 0
    }
  },
  methods: {
    ...mapActions({
      addData: 'apples/addData'
    }),
    async calculate () {
      try {
        let response = await this.$axios.post('http://127.0.0.1:5000/calculate', {
          array: this.nrApples,
          K: this.K,
          L: this.L
        })
        console.log('response', response)
        this.addData({
          total: response.data.total,
          K: this.K,
          L: this.L
        })
        this.$router.push('/apples')
      } catch (err) {
        console.log('error', err)
      }
    }
  }
}
</script>
