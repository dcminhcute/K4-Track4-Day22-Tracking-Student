# Nhật ký thí nghiệm tracking

Mỗi lượt dưới đây xử lý đúng 150 frame đầu của video, dùng detector và weights Re-ID cố định. Mỗi thay đổi ngưỡng được đối chiếu với cùng tracker ở conf=0.3, iou=0.5. Số hộp/ID là thống kê file kết quả, không phải thước đo chính xác hay số lần đổi ID.

| Video | Tracker | conf | iou | Frame đã xử lý | Số hộp track | Số ID | Thư mục kết quả |
|---|---|---|---|---|---|---|---|
| video_1 | botsort | 0.15 | 0.5 | 150 | 978 | 15 | runs/quet/video_1_botsort_c015_i05 |
| video_1 | botsort | 0.3 | 0.4 | 150 | 784 | 13 | runs/quet/video_1_botsort_c03_i04 |
| video_1 | botsort | 0.3 | 0.5 | 150 | 847 | 15 | runs/baseline/botsort_c030_i050 |
| video_1 | botsort | 0.3 | 0.7 | 150 | 905 | 15 | runs/quet/video_1_botsort_c03_i07 |
| video_1 | botsort | 0.5 | 0.5 | 150 | 561 | 10 | runs/quet/video_1_botsort_c05_i05 |
| video_1 | bytetrack | 0.3 | 0.5 | 150 | 651 | 9 | runs/baseline/bytetrack_c030_i050 |
| video_2 | botsort | 0.15 | 0.5 | 150 | 1720 | 21 | runs/quet/video_2_botsort_c015_i05 |
| video_2 | botsort | 0.3 | 0.4 | 150 | 1543 | 23 | runs/quet/video_2_botsort_c03_i04 |
| video_2 | botsort | 0.3 | 0.5 | 150 | 1543 | 23 | runs/baseline/botsort_c030_i050 |
| video_2 | botsort | 0.3 | 0.7 | 150 | 1564 | 24 | runs/quet/video_2_botsort_c03_i07 |
| video_2 | botsort | 0.5 | 0.5 | 150 | 1125 | 14 | runs/quet/video_2_botsort_c05_i05 |
| video_2 | bytetrack | 0.3 | 0.5 | 150 | 1313 | 16 | runs/baseline/bytetrack_c030_i050 |
| video_3 | botsort | 0.3 | 0.5 | 150 | 765 | 23 | runs/baseline/botsort_c030_i050 |
| video_3 | bytetrack | 0.15 | 0.5 | 150 | 597 | 19 | runs/quet/video_3_bytetrack_c015_i05 |
| video_3 | bytetrack | 0.3 | 0.4 | 150 | 593 | 18 | runs/quet/video_3_bytetrack_c03_i04 |
| video_3 | bytetrack | 0.3 | 0.5 | 150 | 593 | 18 | runs/baseline/bytetrack_c030_i050 |
| video_3 | bytetrack | 0.3 | 0.7 | 150 | 593 | 18 | runs/quet/video_3_bytetrack_c03_i07 |
| video_3 | bytetrack | 0.5 | 0.5 | 150 | 553 | 17 | runs/quet/video_3_bytetrack_c05_i05 |
| video_4 | botsort | 0.3 | 0.5 | 150 | 958 | 18 | runs/baseline/botsort_c030_i050 |
| video_4 | bytetrack | 0.15 | 0.5 | 150 | 845 | 13 | runs/quet/video_4_bytetrack_c015_i05 |
| video_4 | bytetrack | 0.3 | 0.4 | 150 | 809 | 15 | runs/quet/video_4_bytetrack_c03_i04 |
| video_4 | bytetrack | 0.3 | 0.5 | 150 | 809 | 15 | runs/baseline/bytetrack_c030_i050 |
| video_4 | bytetrack | 0.3 | 0.7 | 150 | 809 | 15 | runs/quet/video_4_bytetrack_c03_i07 |
| video_4 | bytetrack | 0.5 | 0.5 | 150 | 773 | 17 | runs/quet/video_4_bytetrack_c05_i05 |
| video_5 | botsort | 0.15 | 0.5 | 150 | 994 | 27 | runs/quet/video_5_botsort_c015_i05 |
| video_5 | botsort | 0.3 | 0.4 | 150 | 907 | 27 | runs/quet/video_5_botsort_c03_i04 |
| video_5 | botsort | 0.3 | 0.5 | 150 | 907 | 27 | runs/baseline/botsort_c030_i050 |
| video_5 | botsort | 0.3 | 0.7 | 150 | 916 | 28 | runs/quet/video_5_botsort_c03_i07 |
| video_5 | botsort | 0.5 | 0.5 | 150 | 527 | 17 | runs/quet/video_5_botsort_c05_i05 |
| video_5 | bytetrack | 0.3 | 0.5 | 150 | 673 | 20 | runs/baseline/bytetrack_c030_i050 |

## Đối chiếu toàn bộ chuỗi

- video_3: ByteTrack và BoT-SORT cùng conf=0.3, iou=0.5, đủ 837 frame.
- video_4: ByteTrack và BoT-SORT cùng conf=0.3, iou=0.5, đủ 900 frame.

Các bản chạy kiểm tra cài đặt khi thư mục ảnh chưa giải nén đủ được loại khỏi nhật ký và không dùng chọn cấu hình.

Các nhật ký thời gian dùng thời gian thực, có thể bao gồm lúc máy tạm dừng; không dùng chúng làm benchmark hiệu năng.
