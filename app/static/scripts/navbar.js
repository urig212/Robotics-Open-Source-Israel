window.onscroll = () => {
    const nav = document.querySelector('#navbar');
    if (this.scrollY <= 20)
      nav.className = '';
    else if (this.scrollY <= 150)
      nav.className = 'scroll1'
  };
  