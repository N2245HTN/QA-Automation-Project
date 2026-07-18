describe('Custom Commands', () => {

  it('uses the custom login command', () => {

    cy.login('tomsmith', 'SuperSecretPassword!')

    cy.url().should('include', '/secure')

    cy.get('.flash.success')
      .should('be.visible')

  })

})