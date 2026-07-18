describe('SauceDemo Add Product to Cart Test', () => {

    it('should add a product to the cart successfully', () => {

        // Open website
        cy.visit('https://www.saucedemo.com/');

        // Login
        cy.get('[data-test="username"]')
          .type('standard_user');

        cy.get('[data-test="password"]')
          .type('secret_sauce');

        cy.get('[data-test="login-button"]')
          .click();

        // Verify Products page
        cy.get('.title')
          .should('contain', 'Products');

        // Add Sauce Labs Backpack to cart
        cy.get('[data-test="add-to-cart-sauce-labs-backpack"]')
          .click();

        // Verify cart badge shows 1
        cy.get('.shopping_cart_badge')
          .should('contain', '1');

        // Open cart
        cy.get('.shopping_cart_link')
          .click();

        // Verify product is in cart
        cy.get('.inventory_item_name')
          .should('contain', 'Sauce Labs Backpack');

    });

});