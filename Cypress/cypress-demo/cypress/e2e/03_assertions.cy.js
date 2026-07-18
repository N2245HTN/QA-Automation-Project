describe('Assertion Examples', () => {

  beforeEach(() => {
    cy.visit('https://the-internet.herokuapp.com')
  })

  it('shows common assertion types', () => {
    // Text content
    cy.get('h1').should('have.text', 'Welcome to the-internet')

    // Element visibility
    cy.get('h1').should('be.visible')

    // Element exists — use a selector that actually exists on this page
    cy.get('ul').should('exist')

    // URL / location
    cy.url().should('eq', 'https://the-internet.herokuapp.com/')

    // Count elements
    cy.get('ul li').should('have.length.greaterThan', 5)

    // Attribute check
    cy.get('a[href="/login"]').should('have.attr', 'href', '/login')
  })

})