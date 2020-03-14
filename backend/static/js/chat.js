function toggleFab() {
    $('.prime').toggleClass('zmdi-comment-outline');
    $('.prime').toggleClass('zmdi-close');
    $('.prime').toggleClass('chat-is-active');
    $('.prime').toggleClass('is-visible');
    $('#prime').toggleClass('is-float');
    $('.chat').toggleClass('is-visible');
    $('.chatfab').toggleClass('is-visible');
}

var botui = new BotUI('chat_converse');
botui.message.add({
    content: 'Hola, te gustaria pedir un prestamo?'
});

const chat = new Vue({
    el: '#app',
    data() {
        return {
            message: ''
        }
    },
    methods: {
        saveMessage(message, isHuman) {
            /*Save in localStorage*/
            let chatSession = []
            if (localStorage.chatSession != undefined && localStorage.chatSession.length>0){
                chatSession = JSON.parse(localStorage.chatSession)
            }
            chatSession.push({'message':message,'sender':(isHuman) ? "Human": "Bot"})
            localStorage.chatSession = JSON.stringify(chatSession)
            /*Add Messsage to botui*/
            botui.message.add({
                human: isHuman,
                content: message
            });
        },
        sendMessage() {
            if(this.message== '') return
            this.saveMessage(this.message, true)
            fetch('http://localhost:5005/conversations/test/respond?q=' + this.message + "&token=myToken")
                .then((response) => {
                    return response.json();
                })
                .then((response) => {
                    console.log(response)
                    /*if dont have response, return */
                    if (response.length == 0) return
                    /*check how many messages returns the bot*/
                        /* Iterate for every response */
                        response.forEach((singleResponse) => {
                            /* Save session and add to botui */
                            chat.saveMessage(singleResponse.text,false)
                        });
                });

            this.message = ''
        },
    }
})