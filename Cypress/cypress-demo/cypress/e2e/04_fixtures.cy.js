describe("Using Fixtures", () => {
  it("logs in using fixture data", () => {
    cy.fixture("testData").then((user) => {
      cy.visit("https://www.saucedemo.com/");

      cy.get('[data-test="username"]').type(user.username);
      cy.get('[data-test="password"]').type(user.password);

      cy.get('[data-test="login-button"]').click();

      cy.url().should("include", "/inventory.html");
    });
  });
});
