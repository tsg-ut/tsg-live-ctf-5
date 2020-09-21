<form method="GET">
  <input name="file" type="text" value="<?= $_GET['file'] ?: 'index.php' ?>">
  <button type="submit">Get file</button>
</form>
<?php
if (isset($_GET['file'])) {
  echo '<pre>';
  echo htmlspecialchars(file_get_contents($_GET['file']));
  echo '</pre>';
}