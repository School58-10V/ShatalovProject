<template>
    <div>
        <p>{{ quote }}</p>
    </div>
</template>

<script>
export default {
    name: 'QuoteComponent',
    data() {
        return {
            quote: 'Загрузка...'
        }
    },
    created() {
        this.getQuote();
    },
    methods: {
        getQuote() {
            fetch('http://localhost:5000/quotes/' + this.$route.params.id)
                .then(response => response.json()).then(data => {
                    console.log(data)
                    this.quote = data;
                });
        }
    },
}

</script>

