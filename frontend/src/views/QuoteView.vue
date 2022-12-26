<template>
    <div>
        <h1>Цитата</h1>
        <QuoteComponent />
    </div>
</template>

<script>
import QuoteComponent from '@/components/QuoteComponent.vue'

export default {
    name: 'QuoteView',
    components: {
        QuoteComponent
    },
}
</script>

