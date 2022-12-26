<template>
  <h1>Цитаты</h1>
  <div class="quote" v-for="(item, key) in quoteList" :key="key">
    <SmallQuoteComponent :quote="item" :quoteId="key" @click="redirect()"></SmallQuoteComponent>
  </div>
</template>

<script>
import SmallQuoteComponent from '@/components/SmallQuoteComponent.vue'

export default {
  name: 'HomeView',
  data() {
    return {
      quoteList: []
    }
  },
  created() {
    this.getQuoteList()
  },
  methods: {
    getQuoteList() {
      fetch('http://localhost:5000/quotes').then(res => res.json()).then(data => {
        this.quoteList = data.quotes

        console.log(this.quoteList)
      })
    },
  },
  components: {
    SmallQuoteComponent: SmallQuoteComponent
  }
}
</script>
