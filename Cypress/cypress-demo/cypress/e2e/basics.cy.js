describe('Basic Cypress Demo', () => {

  it('visits a webpage and checks the title', () => {
    cy.visit('https://example.com')
    cy.title().should('include', 'Example Domain')
  })

  it('checks that a heading exists on the page', () => {
    cy.visit('https://example.com')
    cy.get('h1').should('be.visible')
    cy.get('h1').should('contain.text', 'Example Domain')
  })

})