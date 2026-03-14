import json
import csv


def process_orders(file_path):

    with open(file_path, "r") as f:
        data = json.load(f)

    result = []

    for order in data["orders"]:

        order_id = order.get("order_id", "")
        customer_name = order.get("customer", {}).get("name", "")
        address = order.get("shipping_address", "")
        country_code = "US"

        items = order.get("items", [])

        order_total = 0

        for item in items:

            price = item.get("price", 0)
            quantity = item.get("quantity", 0)

            order_total += price * quantity

        discount = 0

        if order_total > 100:
            discount = order_total * 0.10

        for item in items:

            product_name = item.get("name", "")
            price = item.get("price", 0)
            quantity = item.get("quantity", 0)

            total_value = price * quantity

            shipping_cost = quantity * 5

            final_total = total_value - (discount / len(items)) + shipping_cost

            result.append([
                order_id,
                customer_name,
                product_name,
                price,
                quantity,
                total_value,
                round(discount,2),
                shipping_cost,
                round(final_total,2),
                address,
                country_code
            ])

    return result


def save_csv(data):

    headers = [
        "Order ID",
        "Customer Name",
        "Product Name",
        "Product Price",
        "Quantity Purchased",
        "Total Value",
        "Discount",
        "Shipping Cost",
        "Final Total",
        "Shipping Address",
        "Country Code"
    ]

    with open("orders_output.csv", "w", newline="") as f:

        writer = csv.writer(f)

        writer.writerow(headers)

        writer.writerows(data)


def main():

    data = process_orders("sales.json")

    data.sort(key=lambda x: x[8], reverse=True)

    save_csv(data)

    print("CSV file generated: orders_output.csv")


if __name__ == "__main__":
    main()