describe('Form Interactions', () => {

  it('logs into a demo site', () => {
    cy.visit('https://the-internet.herokuapp.com/login')

    cy.get('#username').type('tomsmith')
    cy.get('#password').type('SuperSecretPassword!')
    cy.get('button[type="submit"]').click()

    cy.url().should('include', '/secure')
    cy.get('.flash.success')
      .should('contain', 'You logged into a secure area!')
  })

})