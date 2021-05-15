const toggleMenu = (headerToggle, navbar) => {
    const toggleBtn = document.getElementById(headerToggle);
    const nav = document.getElementById(navbar);

    if (headerToggle && navbar) {
        toggleBtn.addEventListener('click', () => {
            nav.classList.toggle('show-menu');

            toggleBtn.classList.toggle('bx-x');
        })
    }
}

toggleMenu('header-bars', 'navbar');


const links = document.querySelectorAll('.nav-link');

links.forEach(l => {
    if (l.href === location.href)
        l.classList.add('active');
})


function showDiv(divID) {
    let x = document.getElementById(divID);
    if (x.style.display === 'none') {
        x.style.display = 'block';
    } else {
        x.style.display = 'none';
    }
}
