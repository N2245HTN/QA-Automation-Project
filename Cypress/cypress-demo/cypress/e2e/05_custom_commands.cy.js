describe("Custom Commands", () => {
  it("uses the custom login command", () => {
    cy.login("standard_user", "secret_sauce");

    cy.url().should("include", "/inventory.html");
  });
});
