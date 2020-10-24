<link href="https://fonts.googleapis.com/css2?family=Montserrat:ital@1&display=swap" rel="stylesheet">
<nav>
    <div class="logo"></div>
    <div class="hrefs">
<a>Главная
<div class="masc"></div></a>
<a>О boTrade</a>
<a>Команда</a>
<a>Контакты</a>
    </div>
</nav>
<style>
    a {
        text-decoration: none;
        color: #000000;
    }
    nav {
        z-index: 10;
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 60px;
        display: flex;
        justify-content: space-between;
        box-shadow: -1px 8px 22px 1px rgba(70,70,70,0.81);
    }
    .logo {
        height: 100%;
    }
    .hrefs {
        height: 100%;
        width: 600px;
        display: flex;
        justify-content: space-around;
        align-items: center;
        margin: 0 20px;
        font-family: 'Montserrat', sans-serif;
    }
    .hrefs a {
        flex: 1 1;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100%;
    }
    .hrefs a:hover {
        cursor: pointer;
        background-color: #d4d0cf;
    }
</style>