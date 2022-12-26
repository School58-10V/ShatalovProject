<template>
    <div class="small-quote" @click="redirect()">
        <p class="small-quote__text">{{ quote }}</p>
    </div>
</template>


<script>
export default {
    name: "SmallQuoteComponent",
    props: {
        quote: {
            type: String,
            required: true
        },
        quoteId: {
            type: String,
            required: true
        }
    },
    methods: {
        redirect() {
            this.$router.push(`/quote/${this.quoteId}`);
        }
    }
}

</script>

<style>
.small-quote {
    background-color: #f5f5f5;
    padding: 1rem;
    border-radius: 0.5rem;
    margin-bottom: 1rem;
}

.small-quote__text {
    font-size: 1.2rem;
    font-weight: 300;
    color: #333;
}
</style>
