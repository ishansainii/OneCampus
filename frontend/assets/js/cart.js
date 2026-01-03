// assets/js/cart.js

let cart = JSON.parse(localStorage.getItem('cart')) || [];

function addToCart(item, quantity) {
    const existingItem = cart.find(cartItem => cartItem.id === item.id);
    if (existingItem) {
        existingItem.quantity += quantity;
    } else {
        cart.push({ ...item, quantity });
    }
    localStorage.setItem('cart', JSON.stringify(cart));
    updateCartCount();
}

function updateCartCount() {
    const cartCount = cart.reduce((total, item) => total + item.quantity, 0);
    const cartCountElements = document.querySelectorAll('#cart-count');
    cartCountElements.forEach(el => el.textContent = cartCount);
}

document.addEventListener('DOMContentLoaded', () => {
    updateCartCount();
});
