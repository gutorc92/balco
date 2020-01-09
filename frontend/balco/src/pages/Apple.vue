<template lang="pug">
  q-page(class="flex flex-center")
    div(style="width: 30%;" class="column wrap justify-center items-start content-center")
      q-chip(size="40px")
        q-avatar
          img(src="~assets/Farm.svg")
        | Carla {{K}}
      q-chip(size="40px")
        q-avatar
            img(src="~assets/Farmer.svg")
        | Marcelo {{L}}
      q-chip(size="40px")| Total {{apples}}
      q-card(flat class="fit row wrap justify-center items-start content-start")
        q-avatar(v-for="i in apples" :key="i")
          img(src="~assets/Apple.svg")
</template>

<script>
export default {
  name: 'ApplePage',
  computed: {
    apples () {
      return this.$store.getters['apples/getApples']
    },
    K () {
      return this.$store.getters['apples/getK']
    },
    L () {
      return this.$store.getters['apples/getL']
    }
  },
  data () {
    return {
      nrApples: null
    }
  }
}
</script>
