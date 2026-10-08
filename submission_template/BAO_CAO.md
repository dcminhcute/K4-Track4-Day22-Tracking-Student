# Báo cáo lab: chọn tracker cho 5 video

**Nhóm:** khuynmin. **Thành viên:** Trần Ngọc Khuyến; Đoàn Quang Minh.

Detector cố định `yolo26n.pt`, 640 px, lớp người; Re-ID `osnet_x0_25_msmt17.pt`. Chạy CPU trong `.venv`. `conf` và `iou` là ngưỡng tin cậy và NMS của detector, không phải ngưỡng ghép ID.

## 1. CP1 — Dữ liệu, notebook và giả thuyết

Đã kiểm tra dữ liệu tại `lab_data/data_lab21`: năm video có lần lượt 600, 1050, 837, 900, 750 ảnh JPG, tổng 4137 frame. Chỉ video_1 có nhãn. Gói tải về thiếu preview và eval_config: đã tạo preview từ ảnh, bổ sung metadata `benchmark=LAB21`, `split=train`, giữ nguyên nhãn. Preview dùng 30 fps cho video_1 theo seqinfo, 20 fps để xem video_2–5; không khẳng định 20 fps là tốc độ quay gốc.

Notebook đã chạy, lưu đầu ra và hình YOLO, kernel `cv_robotics_lab21 (.venv)`. Đáp án True/False: **True, False, True**. B có nhiều lần đổi ID nên MOTA giảm; chênh HOTA A/B 0,01 nhỏ hơn chênh IDF1 0,10; C có IDF1 cao hơn A nhưng MOTA thấp hơn. Ảnh đầu video_1 có 6 hộp người tại conf=0.3/iou=0.5, **chưa có ID**; conf=0.15 cho 14 hộp, conf=0.5 cho 5 hộp. Một ảnh không đại diện cả chuỗi.

Giả thuyết trước đối chiếu: video_1 có người nhỏ trong bóng râm, giảm conf có thể giảm bỏ sót; video_2 tối và đông, Re-ID có thể hỗ trợ khi che khuất nhưng ngoại hình yếu dễ gây nhầm. Camera di chuyển ở video_3/5 có thể tạo lợi thế cho BoT-SORT, cần kiểm tra thực tế. Video_4 có kính, tăng conf có thể giảm hộp yếu nhưng cũng bỏ người thật phía xa.

## 2. Cấu hình đã chọn

Đã chạy **30 lượt thử**, mỗi lượt 150 frame đầu: cả ByteTrack và BoT-SORT tại 0.3/0.5 cho mỗi video, sau đó chọn một tracker để thử conf=0.15/0.3/0.5 và iou=0.4/0.5/0.7. Mỗi lượt so với baseline chỉ đổi một tham số, lưu thư mục riêng. [Nhật ký đầy đủ](NHAT_KY_THI_NGHIEM.md) ghi cả cấu hình loại; bảng máy đọc nằm tại `runs/nhat_ky_thi_nghiem.csv`.

| Video | Tracker | conf | iou | Quan sát và lý do chọn | Đã thử nhưng loại |
|---|---|---|---|---|---|
| video_1 | botsort | 0.15 | 0.5 | Thêm người nhỏ, tối phía xa; vẫn nhiều người thiếu hộp | BoT-SORT 0.5/0.5 bỏ nhiều người; ByteTrack 0.3/0.5 phủ ít người hơn trong đoạn thử |
| video_2 | botsort | 0.15 | 0.5 | Thêm người có hộp yếu trong cảnh đêm; người đứng bên phải giữ ID ở các mốc xem | BoT-SORT 0.5/0.5 mất nhiều hộp; ByteTrack 0.3/0.5 ít người được theo dõi hơn |
| video_3 | bytetrack | 0.3 | 0.5 | Giữ người chính đoạn đầu; BoT-SORT toàn chuỗi chưa khắc phục rõ lỗi sau che khuất | BoT-SORT 0.3/0.5 vẫn phân mảnh; ByteTrack 0.15/0.5 không cải thiện rõ, 0.5/0.5 giảm hộp yếu |
| video_4 | bytetrack | 0.3 | 0.5 | Theo dõi người gần camera đoạn đầu; BoT-SORT cũng phân mảnh đoạn cuối | BoT-SORT 0.3/0.5 chưa có lợi thế rõ; ByteTrack 0.15/0.5 thêm hộp yếu gần nền/kính, 0.5/0.5 giảm người nền |
| video_5 | botsort | 0.15 | 0.5 | Thêm người phía trái tối khi xe tiếp cận giao lộ | BoT-SORT 0.5/0.5 bỏ nhiều người; ByteTrack 0.3/0.5 phủ ít người hơn đoạn thử |

Đổi iou 0.4/0.5/0.7 ở video_3/4 không tạo khác biệt đáng kể về frame, ID và tọa độ hộp trong đoạn thử. Các video còn lại chưa thấy lợi ích rõ để đổi khỏi 0.5. Không coi tổng hộp/ID là độ chính xác hay IDSW. Hai tracker có các mặc định khác nhau nên không quy toàn bộ khác biệt riêng cho Re-ID. Các lựa chọn conf thấp ưu tiên giảm bỏ sót theo quan sát, chưa chứng minh tối ưu.

Đã chạy thêm BoT-SORT 0.3/0.5 **toàn chuỗi** video_3 và video_4 tại `runs/doi_chieu_day_du/botsort_c030_i050/`. Quan sát dựa trên mốc frame trải khắp chuỗi và ảnh so sánh tại `runs/quan_sat/`, không bảo đảm mọi ID đúng ở mọi frame. Các lượt kiểm tra cài đặt khi ảnh chưa giải nén đủ đã bị loại.

## 3. Số liệu video_1

Chấm đủ 600 frame bằng `scripts/evaluate_practice.py`, run `bai_lab_video_1`. Trích log `runs/nop_bai/video_1_danh_gia.log`:

```text
HOTA   29.343
DetA   19.236
AssA   45.113
MOTA   20.731
IDF1   29.561
CLR_TP 4384
CLR_FN 14197
CLR_FP 505
IDSW   27
Frag   72
```

Các metric HOTA/MOTA/IDF1 ở thang phần trăm. Recall CLEAR 23.594%, precision CLEAR 89.671%. Bỏ sót 14197 lần xuất hiện của người là vấn đề lớn nhất, đặc biệt người nhỏ/tối. Sau tiền xử lý TrackEval còn 4889 detection và 55 ID, khác thống kê thô của file nộp. Chỉ chấm video_1; video_2–5 đánh giá bằng mắt, không tìm hoặc thêm nhãn.

## 4. Phân tích

**Video_1:** Camera tĩnh nhưng nhiều người nền nhỏ và tối. Hạ conf giúp xuất hiện thêm hộp trên người thật ở các mốc so sánh. BoT-SORT được chọn theo độ phủ đoạn thử, song kết quả toàn chuỗi vẫn có khoảng trống và phân mảnh. FN lớn xác nhận rằng giảm conf có ích nhưng chưa đủ giải quyết bỏ sót.

**Video_2:** Ánh sáng không đều, đông người và có cột che khuất. Người đứng mép phải giữ ID4 ở các mốc 1, 150, 350, 550, 700, 1050 trong kết quả chọn. Conf=0.15 giữ thêm hộp yếu so với 0.5, nhưng người phía xa vẫn thiếu hộp. Có dấu hiệu phân mảnh ở người di chuyển gần đám đông; chưa có nhãn để khẳng định giảm IDSW toàn video.

**Video_3:** Camera di chuyển, ảnh nhỏ khiến vị trí và ngoại hình biến đổi mạnh. ByteTrack giữ người áo sọc ID1 và người áo xám ID2 đoạn đầu; đến frame279 ID1 chuyển sang người áo đỏ khác, người áo sọc nhận ID59. BoT-SORT toàn chuỗi cũng mất ID cũ và phân mảnh; người áo đỏ đổi ID giữa mốc 420 và 558. Giữ ByteTrack vì chưa thấy ưu thế rõ, đồng thời ghi nhận lỗi; giả thuyết Re-ID tốt hơn chưa được xác nhận.

**Video_4:** Camera di chuyển trong nhà, có kính và người che nhau. Cả hai tracker giữ người chính đoạn đầu nhưng phân mảnh cuối chuỗi; người áo hồng có ID mới ở frame900. BoT-SORT toàn chuỗi không giải quyết rõ tình huống này. Chọn ByteTrack 0.3/0.5; tăng conf mất thêm hộp yếu, giảm conf chưa có lợi ích rõ và cần xem kỹ vùng phản chiếu.

**Video_5:** Xe đổi hướng mạnh ở giao lộ, vùng sáng/tối chênh nhau. BoT-SORT 0.15 theo dõi thêm người phía trái tối; frame60 có sáu track so với ba tại conf=0.5. Sau khi xe rẽ vẫn có người chưa được đóng hộp và không bảo đảm ID liên tục. Giả thuyết giảm conf hỗ trợ độ phủ có bằng chứng quan sát, lợi ích giữ ID xuyên đoạn rẽ chưa được chứng minh định lượng.

## 5. Kiểm tra bài nộp và tái lập

Mọi lượt tạo file nộp đều bỏ `--max-frames`:

| File trong runs/nop_bai | Frame xử lý/preview | Dòng MOT | ID thô |
|---|---:|---:|---:|
| video_1.txt | 600 | 5179 | 59 |
| video_2.txt | 1050 | 13821 | 62 |
| video_3.txt | 837 | 4271 | 127 |
| video_4.txt | 900 | 5759 | 61 |
| video_5.txt | 750 | 3333 | 79 |

Đã kiểm tra 10 cột MOT, số hữu hạn, frame đúng phạm vi, ID hợp lệ, hộp có kích thước dương, không trùng frame/ID và đọc được frame cuối của cả năm preview. Log, video vẽ ID và `video_N_cau_hinh.json` nằm cạnh file nộp. Kết quả kiểm tra tại `runs/kiem_tra_bai_nop.json`. Bộ kiểm thử repo: **5 passed**. Sửa TrackEval để alias NumPy có hiệu lực trong tiến trình con và dùng backend Agg, kèm kiểm thử hồi quy.

Chạy từ PowerShell tại thư mục gốc:

```powershell
.\.venv\Scripts\Activate.ps1
$env:LAB_DATA = (Resolve-Path '.\lab_data\data_lab21').Path
python scripts/check_data.py --lab-data-root "$env:LAB_DATA"
foreach ($n in 1..5) {
    $tracker = if ($n -in 3,4) { 'bytetrack' } else { 'botsort' }
    $conf = if ($n -in 3,4) { '0.3' } else { '0.15' }
    python scripts/run_tracking.py --source "$env:LAB_DATA/video_$n/img1" --seq-name "video_$n" --tracker $tracker --conf $conf --iou 0.5 --out runs/nop_bai --save-video
}
python scripts/evaluate_practice.py --trackeval-root TrackEval --lab-data-root "$env:LAB_DATA" --submission runs/nop_bai/video_1.txt --run-name bai_lab_video_1
```

Mở notebook từ môi trường có LAB_DATA, chọn kernel `cv_robotics_lab21 (.venv)`. BoxMOT 10.0.42 khai báo NumPy 1.23.1, trong khi Python 3.11 dùng NumPy 1.26.4: `pip check` vẫn báo khác pin này, nhưng tracker, notebook và chấm MOT đã chạy thành công. Danh sách cài đặt tương thích tại `.venv/requirements-compatible.txt`.

## 6. Nếu có thêm thời gian

Thử đoạn dài qua giao cắt và camera rẽ, quét conf mịn hơn quanh giá trị chọn. Xem từng frame chuyển ID ở video_3 và mất track ở video_4; thay detector hoặc trọng số Re-ID chỉ thuộc phần mở rộng.
