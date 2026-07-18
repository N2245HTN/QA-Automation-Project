describe('Full E2E Flow', () => {

  it('complete user journey', () => {

    cy.visit('https://the-internet.herokuapp.com')

    cy.get('h1').should('be.visible')

    cy.get('a[href="/login"]').click()

    cy.url().should('include', '/login')

    cy.get('#username').type('tomsmith')
    cy.get('#password').type('SuperSecretPassword!')

    cy.get('button[type="submit"]').click()

    cy.url().should('include', '/secure')

    cy.get('.flash.success')
      .should('contain', 'You logged into a secure area!')

    cy.get('.button.secondary').click()

    cy.get('.flash')
      .should('contain', 'You logged out')

    cy.url().should('include', '/login')

  })

})