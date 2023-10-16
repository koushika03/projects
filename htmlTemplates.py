css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #F0F2F6
}
.chat-message.bot {
    background-color: #F0F2F6
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #030320;
}
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://as2.ftcdn.net/v2/jpg/03/51/61/49/1000_F_351614912_nhPej8tYdn8gytfBnBPag8HBUt2vaznE.jpg"
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://cdn.vectorstock.com/i/1000x1000/54/41/young-and-elegant-woman-avatar-profile-vector-9685441.webp">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''