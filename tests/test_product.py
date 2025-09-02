from unittest.mock import Mock
from app_products.service import ProductService


def test_get_product_in_price_range():
    # Arrange
    fake_product = Mock()
    fake_product.price = 150

    repo = Mock()
    repo.get_by_id.return_value = fake_product

    service = ProductService(repo)

    # Act
    result, flag = service.get_product(42)

    # Assert
    assert result == fake_product
    assert flag is True
    repo.get_by_id.assert_called_once_with(42)


def test_get_product_outside_range_uses_queryset():
    # Arrange
    fake_qs = Mock()
    fake_filtered = Mock()
    fake_selected = Mock()
    fake_final = Mock()

    fake_qs.price = 300  # теперь условие "if" не выполнится

    # Настраиваем цепочку вызовов .filter().select_related().first()
    fake_qs.filter.return_value = fake_filtered
    fake_filtered.select_related.return_value = fake_selected
    fake_selected.first.return_value = fake_final

    repo = Mock()
    repo.get_by_id.return_value = fake_qs

    service = ProductService(repo)

    # Act
    result, flag = service.get_product(42)

    # Assert
    assert result == fake_final
    assert flag is False
    repo.get_by_id.assert_called_once_with(42)

    fake_qs.filter.assert_called_once_with(id=42)
    fake_filtered.select_related.assert_called_once_with("category")
    fake_selected.first.assert_called_once()

