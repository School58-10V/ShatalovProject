<template>
    <div>
        <label for="quoteText">Текст цитаты</label>
        <input id="quoteText">
        <b-button @click="createQuote()" variant="danger">Создать</b-button>
    </div>

</template>

<script>
export default {
    name: 'CreateQuoteView',
    data() {
        return {
            quote: {
                id: null,
                title: '',
            },
        };
    },
    methods: {
        createQuote() {
            this.quote = document.getElementById('quoteText').value;
            fetch('http://localhost:5000/quotes', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({quote: this.quote}),
            })
            .then(() => {
                this.$router.push({name: 'home'});
            })
        },
    },
}
</script>