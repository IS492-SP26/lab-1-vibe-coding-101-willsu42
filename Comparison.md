# AI Tool Comparison: Pong Game Implementation

This section analyzes the results after creating the same Pong game using three AI tools: **Gemini CLI**, **GitHub Copilot**, and **Cursor**. The comparison focuses on code quality, speed of generation, ease of use, debugging, and flexibility.

---

## Code Quality

**Gemini CLI** produces straightforward and easy-to-follow code, but it relies on a single large game loop, uses magic numbers, and recreates the clock inefficiently, which makes the code harder to maintain or extend.  
**Copilot** improves readability and maintainability through an object-oriented structure and a cleaner game loop, though some design elements feel unfinished and several values remain hardcoded.  
**Cursor** delivers the most refined code, with clear structure, well-defined constants, helpful docstrings, and improved collision handling, making it the most readable, maintainable, and aligned with best practices overall.

---

## Speed of Generation

The TA provided very specific instructions for AI coding, so little time was spent refining prompts. Both **Cursor** and **Copilot** generated a working prototype in under 10 seconds. In contrast, the **Gemini CLI** version took over a minute to generate the code, which may be due to limitations of the terminal-based workflow or local machine performance rather than the model itself.

---

## Ease of Use

**Cursor** is the most intuitive and user-friendly, offering a clean interface and easy model selection directly within the editor.  
**Copilot** in VS Code is less intuitive; invoking the extension to generate code was not immediately obvious, and it was unclear whether it provides a dedicated chat interface. Having multiple AI extensions installed also made the environment feel cluttered.  
**Gemini CLI**, being terminal-based, has the steepest learning curve, with a less smooth interface, slower responses, and a workflow that feels less user-friendly, possibly due to local machine or environment constraints.

---

## Debugging and Error Handling

The **Gemini CLI** version is the hardest to debug because most logic is packed into a single loop, making it difficult to isolate and trace issues.  
The **Copilot** version is easier to debug thanks to its object-oriented structure, although partially implemente
