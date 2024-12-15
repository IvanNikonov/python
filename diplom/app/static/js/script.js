const productForms = document.querySelectorAll('.js-product-form');

if(productForms.length){
    productForms.forEach((element) => {
        element.addEventListener('submit', (e) => {
            e.preventDefault();

            fetch(
            e.target.action, {
                method: e.target.method,
                body: new FormData(e.target)
            })
        })
    })
}