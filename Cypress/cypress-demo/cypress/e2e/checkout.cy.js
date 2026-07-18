describe('SauceDemo Checkout Test', () => {

    it('should complete checkout successfully', () => {

        // Open website
        cy.visit('https://www.saucedemo.com/');

        // Login
        cy.get('[data-test="username"]')
          .type('standard_user');

        cy.get('[data-test="password"]')
          .type('secret_sauce');

        cy.get('[data-test="login-button"]')
          .click();

        // Add product to cart
        cy.get('[data-test="add-to-cart-sauce-labs-backpack"]')
          .click();

        // Open cart
        cy.get('.shopping_cart_link')
          .click();

        // Click Checkout
        cy.get('[data-test="checkout"]')
          .click();

        // Fill customer information
        cy.get('[data-test="firstName"]')
          .type('Nutan');

        cy.get('[data-test="lastName"]')
          .type('Kafle');

        cy.get('[data-test="postalCode"]')
          .type('44600');

        // Continue
        cy.get('[data-test="continue"]')
          .click();

        // Verify checkout overview page
        cy.get('.title')
          .should('contain', 'Checkout: Overview');

        // Finish order
        cy.get('[data-test="finish"]')
          .click();

        // Verify successful order
        cy.get('.complete-header')
          .should('contain', 'Thank you for your order!');

    });

});