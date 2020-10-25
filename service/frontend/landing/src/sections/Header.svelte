<link href="https://fonts.googleapis.com/css2?family=Montserrat:ital@1&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Oswald:wght@200;700&display=swap" rel="stylesheet">
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
    }
    .logo {
        height: 100%;
    }
    .hrefs {
        height: 100%;
        width: 450px;
        display: flex;
        justify-content: space-around;
        align-items: center;
        font-family: 'Oswald', sans-serif;
        margin: 0 20px 0 0;
    }
    .hrefs a {
        flex: 1 1;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100%;
        color: #FFFFFF;
        letter-spacing: 2px;
    }
    .hrefs a:hover {
        cursor: pointer;
    }
</style>