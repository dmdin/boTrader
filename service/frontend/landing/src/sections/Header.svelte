<nav>
  <div class="logo"></div>
  <div class="hrefs">
    <a href="#">Главная</a>
    <a href="./#about">О boTrade</a>
    <a href="https://2d-team.now.sh">Команда</a>
  </div>
</nav>
<style>
  @media all and (max-width: 900px) {
    nav {
      display: none;
    }
  }

  @media all and (min-width: 900px) {
    nav {
      display: flex;
    }
  }

  a {
    text-decoration: none;
    color: #000000;
  }

  nav {
    z-index: 20;
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 60px;
    justify-content: space-between;
  }

  .logo {
    height: 100%;
  }

  .hrefs {
    height: 100%;
    width: 500px;
    display: flex;
    justify-content: space-around;
    align-items: center;
    font-family: Montserrat, sans-serif;
    font-weight: 300;
    font-style: italic;
    margin: 0 20px 0 0;
  }

  .hrefs a {
    flex: 1 1;
    z-index: 21;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100%;
    color: #FFFFFF;
    letter-spacing: 2px;
    font-size: 1.4em;
    transition: all 0.5s ease;
  }

  .hrefs a:hover {
    cursor: pointer;
    text-shadow: 0 0 1px white;
  }
</style>