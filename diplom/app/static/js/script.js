const productForms = document.querySelectorAll('.js-product-form');

if(productForms.length){
    productForms.forEach((element) => {
        element.addEventListener('submit', async (e) => {
            e.preventDefault();

            let response = await fetch(
                e.target.action, {
                method: e.target.method,
                body: new FormData(e.target)
            })

            if (response.ok) {
                alert("Товар добавлен в корзину")
            }
        })
    })
}